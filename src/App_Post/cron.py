import time
import requests
import json
from importlib import reload
from django.contrib.auth.models import User
from App_Login.models import UserProfile
from App_Post.models import OJStanding

def my_job():
    users = UserProfile.objects.all()
    if(OJStanding.objects.all().count() > 0):
        OJStanding.objects.all().delete()
    for u in users:
        try:
            res_data = requests.get('https://uhunt.onlinejudge.org/api/ranklist/' + u.uva_id + '/1/1')
            res_data_cf = requests.get('https://codeforces.com/api/user.status?handle=' + u.codeforces_username + '&from=1&count=1000')
            if(res_data.status_code == 200 and res_data_cf.status_code == 200):
                codeforces_ac = 0
                data = res_data.json()
                data2 = res_data_cf.json()['result']

                if(res_data_cf.json()['status'] == 'OK'):
                    for d in data2:
                        if(d['verdict'] == 'OK'):
                            codeforces_ac += 1
                        
                uva_id = data[1]['userid']
                uva_username = data[1]['username']
                uva_submission = data[1]['ac']
                uva_ranking = data[1]['rank']
                uva = OJStanding(uva_id=uva_id,uva_username=uva_username,uva_submission=uva_submission,
                    uva_ranking=uva_ranking,codeforces_username=u.codeforces_username,
                    codeforces_submission=codeforces_ac)
                uva.user = u.user
                print('saving to DB.....')
                uva.save()
                time.sleep(2)
            else:
                print('Cant find Data')
        except Exception as e:
            print(e)
