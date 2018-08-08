from django.shortcuts import render, redirect
import requests
import wikipedia

# Create your views here.
def index(request):
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
        'real_page_content': real_page_content,
        'real_page_html': real_page_html,
    }
    return render(request, 'hip_hop_production/index.html', context)