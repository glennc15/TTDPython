from django.shortcuts import redirect, render
from django.core.exceptions import ValidationError
# from django.http import HttpResponse
# from django.shortcuts import render
from lists.forms import ItemForm, ExistingListItemForm
from lists.models import Item, List

# Create your views here.
def home_page(request):
	# if request.method == 'POST':
		# Item.objects.create(text=request.POST['text'])
		# return redirect('/lists/the-only-list-in-the-world/')
		# # return redirect('/')

	return render(request, 'home.html', {'form': ItemForm()})





def view_list(request, list_id):
	list_ = List.objects.get(id=list_id)
	form = ExistingListItemForm(for_list=list_)

	if request.method == 'POST':
		form = ExistingListItemForm(for_list=list_, data=request.POST)

		if form.is_valid():
			# Item.objects.create(text=request.POST['text'], list=list_)
			form.save()
			return redirect(list_)
	
	return render(request, 'list.html', {'list': list_, 'form': form})

 

def new_list(request):
	form = ItemForm(data=request.POST)

	if form.is_valid():
		list_ = List.objects.create()
		form.save(for_list=list_)
		# Item.objects.create(text=request.POST['text'], list=list_)
		return redirect(list_)

	else:
		return render(request, 'home.html', {'form': form})

	# try:
	# 	item.full_clean()
	# 	item.save()
	# except ValidationError:
	# 	list_.delete()
	# 	error = "You can't have an empty list item"
	# 	return render(request, 'home.html', {'error': error})

	# return redirect(list_)


# def view_list(request, list_id):
# 	list_ = List.objects.get(id=list_id)
	

# 	if request.method == 'POST':
# 		try:
# 			item = Item.objects.create(text=request.POST['text'], list=list_)
# 			item.full_clean()
# 			item.save()
# 			return redirect(list_)

# 		except ValidationError:
# 			item.delete()
# 			error = "You can't have an empty list item"

# 	# items = Item.objects.filter(list=list_)

# 	form = ItemForm()
# 	return render(request, 'list.html', {'list': list_, 'form': form, 'error': error})


# def add_list(request, list_id):
# 	list_ = List.objects.get(id=list_id)

# 	Item.objects.create(text=request.POST['text'], list=list_)

# 	return redirect(f'/lists/{list_.id}/') 