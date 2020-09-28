import os
import random
from django.shortcuts import render, redirect
from . import util
import markdown
from django.core.files.storage import default_storage
from django.views.decorators.csrf import csrf_protect
from django import forms
from django.contrib import messages

md = markdown.Markdown()

def index(request):
    """Render main page"""

    # Render index
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries(),
    })

def search(request):
    """Render a page or a search-results page if there is a substring match"""
        
    # User reached route via POST (as submitting a form via POST)
    if request.method == "POST":
        query = request.POST.get("q")
        entry = util.get_entry(query)
        
        # look for substring matches
        if not entry:
            entries = util.list_entries()
            matches = []
            matches.clear()
                       
            for entry in entries:
                if query.lower() in entry.lower():
                    matches.append(entry)
              
            return render(request, "encyclopedia/search.html", {
                "entries": matches
            })

        # render entry page
        else:
            entry = md.convert(entry)
            return render(request, "encyclopedia/page.html", {
                "title": query.capitalize(),
                "entry": entry,
            })


def page(request, title):
    """Render requested page"""

    # Look for prompted title in the entry registry
    entry = util.get_entry(title)
    if not entry:
        return render(request, "encyclopedia/notfound.html")
    else:
        entry = md.convert(entry)
        return render(request, "encyclopedia/page.html", {
            "title": title.capitalize(),
            "entry": entry
        })

def entry (request):
    """Create a new entry"""

    # User reached route via POST (as submitting a form via POST)
    if request.method == "POST":
        title = request.POST.get("newtitle")
        content = request.POST.get("newcontent")
        # Check for inputs left unfilled
        if not title or not content:
            data = dict()
            messages.error(request, "Submission failed: Please complete al the fields before submiting")
            return render(request, "encyclopedia/entry.html", data)

        # Check if the page already exists
        filename = f"entries/{title}.md"
        if default_storage.exists(filename):
            data = dict()
            messages.error(request, "Submission failed: A page with this title already exists")
            return render(request, "encyclopedia/entry.html", data)

        # Write a new MD file
        else:
            with open("entries/" + title.capitalize() + ".md", "w", newline="") as file:
                file.seek(0)
                file.write(f"# {title.capitalize()}\n\n{content}")
            file.close()
            return redirect("page", title=title)
                
    return render(request, "encyclopedia/entry.html")

def edit (request):
    """Edit an existing entry"""
    
    # Get the title of the entry as a key to to render the content in textarea
    title = request.POST.get("title")    
    content = util.get_entry(title)
    return render(request, "encyclopedia/edit.html", {
        "content":content,
        "title":title
    })    
 
def save(request):
    """Save the edited entry"""

    # User reached route via POST (as submitting a form via POST)
    if request.method =="POST":
        title = request.POST.get("title")
        editedcontent = request.POST.get("editedcontent")

        # Write new file with same title and different content
        with open("entries/" + title.capitalize() + ".md", "w", newline="") as file:
            file.seek(0)
            file.write(f"{editedcontent}")
        file.close()
        
        return redirect("page", title=title)


def random_page(request):
    """Redirect to a random page"""

    entries = util.list_entries() 
    selected_page = random.choice(entries)
    return redirect("page", title=selected_page)