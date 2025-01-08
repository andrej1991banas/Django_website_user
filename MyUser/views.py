from django.shortcuts import render, redirect
from .forms import CreateUserForm

from .models import Member


def register(request):
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('additional')  # Redirect to the login page after successful registration
    else:
        form = CreateUserForm()

    return render(request, 'register.html', {'form': form})

def homepage(request):
    return render(request, 'homepage.html')

def add_info(request):

    if request.method == 'POST':
        # Fetch data from the form submission
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        try:
            member = Member.objects.create(
                firstname=firstname,
                lastname=lastname,
                email=email,
                phone=phone,
                address=address
                )
            member.save()  # This will save the data to the database

        except Exception as e:
            print(f"An error occurred: {e}")  # Add proper error handling in production


        return render(request, 'add_info.html', {
            'firstname': firstname,
            'lastname': lastname,
            'email': email,
            'phone': phone,
            'address': address
})
    return render(request, 'add_info.html')


