from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import TransferForm
from .models import Transaction, Customer
from django.contrib.auth.decorators import login_required
from .decorators import group_required

# Create your views here.

@group_required('AdminGroup')
@login_required
def customer_list(request):
    customers = Customer.objects.all()
    return render(request, 'bank_app/customer_list.html', {'customers': customers})



@login_required
def transfer_money(request):
    if request.method == 'POST':
        form = TransferForm(request.POST)
        if form.is_valid():
            sender = form.cleaned_data['sender']
            receiver = form.cleaned_data['receiver']
            amount = form.cleaned_data['amount']

            if sender == receiver:
                messages.error(request, "Sender and receiver cannot be the same.")
            elif sender.balance < amount:
                messages.error(request, "Insufficient balance.")
            else:
                # Update balances
                sender.balance -= amount
                receiver.balance += amount
                sender.save()
                receiver.save()

                # Record transaction
                Transaction.objects.create(sender=sender, receiver=receiver, amount=amount)
                messages.success(request, "Transaction successful!")
                return redirect('customer_list')
    else:
        form = TransferForm()

    return render(request, 'bank_app/transfer.html', {'form': form})



from django.db.models import Q
from django.utils import timezone

@login_required
def transaction_history(request):
    query = request.GET.get('q')
    transactions = Transaction.objects.all().order_by('-timestamp')

    if query:
        transactions = transactions.filter(
            Q(sender__name__icontains=query) |
            Q(receiver__name__icontains=query)
        )
    
    return render(request, 'bank_app/transaction_history.html', {
        'transactions': transactions,
        'query': query or ''
    })




from django.db.models import Sum
from django.core.serializers.json import DjangoJSONEncoder
import json

@login_required
def dashboard(request):
    total_customers = Customer.objects.count()
    total_transactions = Transaction.objects.count()
    total_balance = Customer.objects.aggregate(Sum('balance'))['balance__sum'] or 0

    # Chart data: total sent per customer
    customer_data = (
        Transaction.objects
        .values('sender__name')
        .annotate(total_sent=Sum('amount'))
        .order_by('-total_sent')
    )

    chart_labels = [item['sender__name'] for item in customer_data]
    chart_values = [float(item['total_sent']) for item in customer_data]

    return render(request, 'bank_app/dashboard.html', {
        'total_customers': total_customers,
        'total_transactions': total_transactions,
        'total_balance': total_balance,
        'chart_labels': json.dumps(chart_labels, cls=DjangoJSONEncoder),
        'chart_values': json.dumps(chart_values, cls=DjangoJSONEncoder),
    })





from django.contrib.auth import authenticate, login, logout
from .forms import RegisterForm

def register_user(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Account created! Please login.")
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'bank_app/register.html', {'form': form})

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, "Invalid username or password.")
    return render(request, 'bank_app/login.html')

def logout_user(request):
    logout(request)
    return redirect('login')


from django.shortcuts import get_object_or_404

@login_required
def customer_detail(request, pk):
    customer = get_object_or_404(Customer, pk=pk)
    sent_txns = Transaction.objects.filter(sender=customer)
    received_txns = Transaction.objects.filter(receiver=customer)
    return render(request, 'bank_app/customer_detail.html', {
        'customer': customer,
        'sent_txns': sent_txns,
        'received_txns': received_txns
    })



from django.template.loader import get_template
from django.http import HttpResponse
from xhtml2pdf import pisa

@login_required
def export_transactions_pdf(request):
    transactions = Transaction.objects.all().order_by('-timestamp')
    template_path = 'bank_app/pdf_template.html'
    context = {'transactions': transactions}

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="transaction_report.pdf"'
    
    template = get_template(template_path)
    html = template.render(context)

    pisa_status = pisa.CreatePDF(html, dest=response)
    if pisa_status.err:
        return HttpResponse('PDF generation failed: %s' % pisa_status.err)
    return response
       