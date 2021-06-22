res = ""

for i in range(1,61):
    s = input()
    s= s[4:]
    k = '<!-- qat'+str(i)+' --><div class="modal fade" id="qat'+str(i)+'"tabindex="-1" aria-labelledby="qat'+str(i)+'Label" aria-hidden="true"><div class="modal-dialog"><div class="modal-content"><div class="modal-header"><h5 class="modal-title" id="qat'+str(i)+'Label">Вопрос '+str(i)+'</div><div class="modal-body">'+s+'<div class="form-check"><input class="form-check-input" type="radio" name="flexRadioDefault" id="qat'+str(i)+'T"><label class="form-check-label" for="qat'+str(i)+'T">Скорее да</label></div><div class="form-check"><input class="form-check-input" type="radio" name="flexRadioDefault" id="qat'+str(i)+'F" checked><label class="form-check-label" for="qat'+str(i)+'F">Скорее нет</label></div></div><div class="modal-footer"><button type="button" data-bs-toggle="modal" data-bs-target="#qat'+str(i+1)+'" aria-label="Close" class="btn btn-primary">Дальше</button></div></div></div></div>'
    res +=k
print(res)