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

def page(request, title):
    """Render requested page"""

    # User reached route via POST (as submitting a form via POST)
    if request.method == "POST":
        query = request.POST.get("q")
        entry = util.get_entry(query)
        if not entry:
            return render(request, "encyclopedia/page.html", {
                "title": "404",
                "entry": "<h1>Page not found<h1>",
            })
        else:
            entry = md.convert(entry)
            return render(request, "encyclopedia/page.html", {
                "title": query.capitalize(),
                "entry": entry,
            })
    else:
        # Look for prompted title in the entry registry
        entry = util.get_entry(title)
        if not entry:
            return render(request, "encyclopedia/page.html", {
                "title": "404",
                "entry": "<h1>Page not found<h1>"
            })
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
            with open(os.path.join("C:\\Agustin\\cs50-web\\wiki\\entries", f"{title.capitalize()}.md"), "w") as entry:
                entry.write(f"# {title.capitalize()}\n\n{content}")
            return redirect("page", title=title)
                
    return render(request, "encyclopedia/entry.html")

def edit (request):
    """Edit an existing entry"""

    return render(request, "encyclopedia/edit.html")

def random_page(request):
    """Redirect to a random page"""

    entries = util.list_entries() 
    selected_page = random.choice(entries)
    return redirect("page", title=selected_page)