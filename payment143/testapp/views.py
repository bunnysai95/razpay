from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import  ApplicationFormClass,Qrcode
import random
import razorpay
client = razorpay.Client(auth=("rzp_live_7jAYHrhRwvQeDL", "sOpx2gGMUaDtNUXPMcPLyPmB"))


# Create your views here.
# def app(request):
#     return render(request, 'app.html')



def app(request):
    if request.method=='POST':
        fname = request.POST.get("fname")
        lname = request.POST.get("lname")
        dob = request.POST.get('dob')
        board = request.POST.get('board')
        father = request.POST.get("father")
        mother = request.POST.get("mother")
        qualification = request.POST.get('qualification')
        sname = request.POST.get('sname')
        saddress = request.POST.get('Saddress')
        haddress = request.POST.get('Haddress')
        state = request.POST.get('state')
        anum = request.POST.get('anum')
        phonenum = request.POST.get('num')
        email = request.POST.get('email')
        personphoto =request.FILES.get('photo', '')
        signaturephoto = request.FILES.get('signature', '')

        number = '19'+'{:03d}'.format(random.randrange(1, 999))
        username = (state + board + qualification+ number)

        # password = dob
        af = ApplicationFormClass(firstName = fname, lastName = lname, date_of_birth = dob, board = board, fatherName = father, motherName = mother, qualification = qualification, schoolName = sname, schoolAddress = saddress, homeAddress = haddress, aadharNumber = anum, phoneNumber = phonenum, emailID = email, personPhoto = personphoto,  signaturePhoto = signaturephoto,state = state, username = username)
        af.save()
        return redirect('/pay')
        # return HttpResponse('student profile add successfully')
        # return redirect('/stuprofile')

    return render(request, 'app.html')




def payment(request):
     # DATA = { 'amount': '49900', 'currency': 'INR', 'receipt': '874152' };
     # xyz=client.order.create(data= DATA)
     # order_id=xyz.order_id
    return render(request, 'pay.html',{'orderid':'123456'})

def payment2(request):
    if request.method == 'POST':
        tid = request.POST.get('tid')
        tphn = request.POST.get('tphn')
        payment2 = Qrcode(TRANSACTION_ID =tid, PHONE_NUMBER = tphn)
        payment2.save()

        # client = razorpay.Client(auth=("rzp_live_jQyLwPmuoYNk2k", "U7G4m37FawIppW8aVpYDPsuB"))
        # params_dict = { params
        # 'razorpay_order_id': '12122',
        # 'razorpay_payment_id': '332’,
        # 'razorpay_signature': '23233'
        # }
        # client.utility.verify_payment_signature(params_dict) // This is the method

        return HttpResponse('data saved sucessfully')
    return render(request, 'payment.html')

