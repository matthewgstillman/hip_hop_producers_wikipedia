from django.shortcuts import render, redirect
import requests
import wikipedia

# Create your views here.
def index(request):
    if request.method == 'POST':
        producer = request.POST['producer']
        request.session['producer'] = producer
        context = {
            'producer': producer,
        }
        return render(request, 'hip_hop_production/index.html', context)
    else:
        context = {
        }
        return render(request, 'hip_hop_production/index.html', context)

def form(request):
    if request.method == 'POST':
        producer = request.POST['producer']
        request.session['producer'] = producer
        wiki_page = wikipedia.WikipediaPage(title=producer)
        wiki_page_content = wiki_page.content
        wiki_page_html = wiki_page.html()
        print ("Wiki Page Content: " + wiki_page_content)
        wiki_page_search = wikipedia.search(producer)
        wiki_page = wikipedia.page(producer)
        print("Wiki Page: " + str(wiki_page))
        wiki_page_id = wiki_page.pageid
        print("Page ID: " + str(wiki_page_id))
        wiki_page_title = wiki_page.title
        print("Title: " + str(wiki_page_title))
        wiki_page_categories = wiki_page.categories
        print("Categories: " + str(wiki_page_categories))
        wiki_page_summary = wiki_page.summary
        print("Summary: " + str(wiki_page_summary))
        wiki_page_images = wiki_page.images
        print("Images: " + str(wiki_page_images))
        wiki_page_links = wiki_page.links
        print("Links: " + str(wiki_page_links)) 
        wiki_page_sections = wiki_page.sections
        print("Sections: " + str(wiki_page_sections))
        print("Producer: " + str(producer))
        print("Wiki Page: " + str(wiki_page))
        context = {
            'producer': producer,
            'wiki_page': wiki_page,
            'wiki_page_content': wiki_page_content,
            'wiki_page_html': wiki_page_html,
            'wiki_page_search': wiki_page_search,
            'wiki_page_id': wiki_page_id,
            'wiki_page_title': wiki_page_title,
            'wiki_page_categories': wiki_page_categories,
            'wiki_page_summary': wiki_page_summary,
            'wiki_page_images': wiki_page_images,
            'wiki_page_links': wiki_page_links,
            'wiki_page_sections': wiki_page_sections,

        }
        return render(request, 'hip_hop_production/result.html', context)
    else:
        context = {
        }
        return render(request, 'hip_hop_production/index.html', context)
       

def murda_beatz(request):
    url = ("http://en.wikipedia.org/w/api.php?action=query&prop=info&format=json&titles=Murda_Beatz")
    response = requests.get(url)
    index = response.json()
    # wikipedia = MediaWiki()
    real_page = wikipedia.WikipediaPage(title="Murda Beatz")
    real_page_content = real_page.content
    real_page_html = real_page.html()
    print real_page_content
    murda_search = wikipedia.search("Murda Beatz")
    murda_beatz_page = wikipedia.page("Murda Beatz")
    print("Page: " + str(murda_beatz_page))
    murda_beatz_pageid = murda_beatz_page.pageid
    print("Page ID: " + str(murda_beatz_pageid))
    murda_beatz_title = murda_beatz_page.title
    print("Title: " + str(murda_beatz_title))
    murda_beatz_categories = murda_beatz_page.categories
    print("Categories: " + str(murda_beatz_categories))
    murda_beatz_summary = murda_beatz_page.summary
    print("Summary: " + str(murda_beatz_summary))
    murda_beatz_images = murda_beatz_page.images 
    print("Images: " + str(murda_beatz_images))
    murda_beatz_links = murda_beatz_page.links 
    print("Links: " + str(murda_beatz_links))
    murda_beatz_sections = murda_beatz_page.sections 
    print("Sections: " + str(murda_beatz_sections))
    print("Response: " + str(response))
    print("Index: " + str(index))
    print("Real Page: " + str(real_page))
    murda_beatz_wiki_images = murda_beatz_page.images
    context = {
        'response': response,
        'index': index,
        'murda_search': murda_search,
        'murda_beatz_links': murda_beatz_links,
        'murda_beatz_categories': murda_beatz_categories,
        'murda_beatz_images': murda_beatz_images,
        'murda_beatz_summary': murda_beatz_summary,
        'murda_beatz_page': murda_beatz_page,
        'murda_beatz_sections': murda_beatz_sections,
        'murda_beatz_title': murda_beatz_title,
        'murda_beatz_wiki_images': murda_beatz_wiki_images,
        'real_page_content': real_page_content,
        'real_page_html': real_page_html,
    }
    return render(request, 'hip_hop_production/murda_beatz.html', context)


def result(request):
    return render(request, 'hip_hop_production/result.html')