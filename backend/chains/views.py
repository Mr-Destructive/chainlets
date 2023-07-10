from django.shortcuts import render
import google.generativeai as palm
from django.conf import settings

from .models import Chain


def index(request):
    return render(request, 'index.html')

def prompt(request):
    if request.method == "POST":
        palm.configure(api_key=settings.PALM_API_KEY)
        prompt_text = request.POST["prompt"]
        words = request.POST.get("words", 20)
        if prompt_text:
            prompt = f"Give correct, existing {words} words for {prompt_text},the words should be equally distributed from a-z as start and end letters of the words. Only give pure text words and nothing else, seperate each word with a new-line character, only give the words and not letters."
            response = palm.generate_text(prompt=prompt)
            print(response.__dict__)
            words_list = response.candidates[0]['output'].split('\n')
            if len(words_list) > 20:
                chain = Chain.objects.create(prompt=prompt_text, words=",".join(words_list))
                return render(request, 'chains/words.html', context={'words': words_list, 'chain': chain})
    return render(request, 'chains/prompt.html')

def chain(request):
    if request.method == "POST":
        prompt = request.POST.get('prompt')
        print(prompt)
        print(Chain.objects.all()[0].__dict__)
        chain = Chain.objects.filter(prompt__icontains=prompt).first()
        words = chain.words.split(',')
        return render(request, 'chains/words.html', context={'prompt': chain.prompt, 'words': words})
    return render(request, 'chains/prompt.html')
