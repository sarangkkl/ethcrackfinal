from ast import Try
import csv
import pandas as pd
from sympy import public
from home.models import CrytoAcc,MoneyAcc
from django.shortcuts import render,redirect
import string
import ethereum.utils
# import web3
from tqdm import tqdm,trange
# from sha3 import keccak_256

import random



# private_key = keccak_256(token_bytes(32)).digest()
# public_key = PublicKey.from_valid_secret(private_key).format(compressed=False)[1:]
# addr = keccak_256(public_key).digest()[-20:]

# print('private_key:', private_key.hex())
# print('eth addr: 0x' + addr.hex())


def generate_random():
    N = 64
    res = ''.join(random.choices('a'+'b'+'c'+'d'+'e'+'f'+string.digits, k = N))
    return str(res)
   


def index(request): 
    for i in trange(100000):
        key = generate_random()
        try:
            my_address = ethereum.utils.privtoaddr(key).hex()
            my_address = my_address.lower()
            my_address = f"0x{my_address}"
            x = CrytoAcc.objects.get(address=my_address)
            y = MoneyAcc.objects.create(private_key=key,public_key=x.address,blance = x.balance)
            y.save()
            print("got hit",key)
        except:
            pass

    # pk = keys.PrivateKey(private_key)
    # pk = web3.toBytes(hexstr=private_key)

    # obj = CrytoAcc.objects.get(address="0x057549987e849d4dcc9497fdba64abe6bbfc1e62")
    # print(f"The obj i have found is {pk} and it balance is {obj.balance} ")
    return render(request,"index.html")



def csv_reader(file_obj):
    reader = csv.DictReader(file_obj,delimiter=',')
    for line in reader:
        print(line["HolderAddress"]),
        print(line["Balance"])


def handle_submit(request):
    if request.method == 'POST':
        file = request.POST.get('file')
        data = pd.read_csv(file)
        df = pd.DataFrame(data,columns=['HolderAddress','Balance'])
        for ind in df.index:
            x = CrytoAcc.objects.create(address=df['HolderAddress'][ind],balance=df['Balance'][ind])
            x.save()  
    return redirect('/')
