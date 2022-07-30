my_dict = {
    'Dave':'001',
    'Ava':'002',
    'Joe':'003'
}

new_dict = dict(Dave='001', Ava='002',Carlos='003')
#print(new_dict['Dave'])

new_dict2 = {'Employee':{'Dave':{'LastName':'Kelley','Age':22},
                        'Ana':{'LastName':'Martinez','Age':24},
                        'Carlos':{'LastName':'Gonzalez','Age':25}}}

new_dict2['Employee']['Ernesto'] = {'LastName':'Johnson','Age':29}
print(new_dict2)

print(new_dict2['Employee']['Dave']['LastName'])
del(new_dict2['Employee']['Dave'])
print(new_dict2)
