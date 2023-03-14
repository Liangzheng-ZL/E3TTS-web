import inspect
import os 
from pathlib import Path
import dominate
from dominate.tags import *
from dominate.util import raw

from templates import header, authors_row
from templates.audios import audio_table


if __name__ == "__main__":
    # Where to save the generated file.
    root_path = Path(inspect.getfile(inspect.currentframe())).parent
    doc = dominate.document(title=None)

    with doc.head:
        meta(charset="utf-8")
        meta(http_equiv="X-UA-Compatible", content="IE=edge")
        meta(name="viewport", content="width=device-width, initial-scale=1")
        title("BEdit-TTS Online Supplement")
        link(href="./statics/bootstrap-5.2.2-dist/css/bootstrap.min.css", rel="stylesheet")

    with doc:
        # Title and Metadata:
        with div(cls="container").add(div(cls="row")):
            with div(cls="border border-2 bg-light p-5 rounded mt-3 border-dark"):
                header(title="BEdit-TTS: Text-Based Speech Editing System with Bidirectional Transformers", sub="Online Supplement")
                br()

            with div(cls="border border-2 bg-light p-5 rounded mt-3 border-danger"):
                p(
                    "If you are having problems with the audios playing, you can download all audio files on this page",
                    " by downlading this ",
                    a("github repository", href="https://anonymous.4open.science/r/bedit_web-9718"),
                    ". ", 
                    br(), br(),
                    "Some of the page's functionality requires javascript. Try to open with a different up-to-date browser. ",
                    cls="lead"
                )

            with div(cls="border border-2 bg-light p-5 rounded mt-3 border-dark"):
                from abstract import section_abstract
                section_abstract()

            with div(cls="border border-2 bg-light p-5 rounded mt-3 border-dark"):
                from replacement import section_replace_compare
                section_replace_compare()
                
            with div(cls="border border-2 bg-light p-5 rounded mt-3 border-dark"):
                from insertion import section_insert_compare
                section_insert_compare()

            with div(cls="border border-2 bg-light p-5 rounded mt-3 border-dark"):
                from deletion import section_delete_compare
                section_delete_compare()
            
            with div(cls="border border-2 bg-light p-5 rounded mt-3 border-dark"):
                from length_roubtness import section_length_compare
                section_length_compare()
            with div(cls="border border-2 bg-light p-5 rounded mt-3 border-dark"):
                from unseen import section_unseen_compare
                section_unseen_compare()
        
    with doc.footer:
        script(src="./statics/jquery/jquery-1.12.4.min.js")
        script(src="./statics/bootstrap-5.2.2-dist/bootstrap.min.js")

    # Script for allowing only one audio to play at the same time:
    doc.children.append(script(raw("""
        $(function(){
            $("audio").on("play", function() {
                $("audio").not(this).each(function(index, audio) {
                    audio.pause();
                    audio.currentTime = 0;
                });
            });
        });
        """)
    ))

    with open(root_path / "index.html", "w") as index:
        index.write(doc.render())
