import plivo
Auth_Id = 'MAM2E0YWIYMGY5NDY0MJ'
Auth_Token = 'ZTdmYTFkYjk1MDkxODM4ZDRiNzhhODk0MmUxMWZj'
client = plivo.RestClient('Auth_Id','Auth_Token')
response = client.messages.create(
         src='<6303595458>',
         dst='<9866250045>',
         text='python msg',)
print(response)