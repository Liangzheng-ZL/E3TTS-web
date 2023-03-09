"""
HTML generator for Section: Comparison with GuidedTTS 2.
"""

from dominate.tags import *
from dominate.util import raw
from templates.audios import audio_table, my_audio_table
from templates.spinspy import nav_spin


def section_insert_compare():
    h3("Insertion")
    p(
        [
            """Each sample has 4 audios, of which are synthesized audios from baseline and proposed systems. """,
        ], _class="lead"
    )
    h4("Short")
    blocks = []
    def _gen_table(length: str, language: str, o_text: str, e_text: str, name: str):
        return my_audio_table(
            o_text=o_text,
            e_text=e_text,
            audio_files=[
                f"./samples/insert/{language}/{length}/{sys}/{name}.wav" for sys in (
                    "gt", "baseline1", "baseline2", "baseline3", "bedit-tts",
                )
            ],
            titles=[
                f"Original audio", "Baseline 1", "Baseline 2", "Baseline 3", "BEdit-TTS"
            ],
            width=5, control_width_px=250
        )
    blocks.append(_gen_table("short", "eng",
        "Original text: " + """Irreverently tearing open her mother's telegram and reading it as she came.""",
        "Edited text: " + """Irreverently tearing open her  <u><em><strong>young</strong></em></u> mother's telegram and reading it as she came.""",
        "92_auntcretesemancipation_01_hill_0029"
    ))

    blocks.append(_gen_table("short", "eng",
        "Original text: " + """Or whatever was the present task.""",
        "Edited text: " + """Or whatever was the <u><em><strong>new</strong></em></u> present task.""",
        "92_auntcretesemancipation_01_hill_0039"
    ))
    blocks.append(_gen_table("short", "eng",
        "Original text: " + """ Many others have already gone broke.""",
        "Edited text: " + """<u><em><strong>There're</strong></em></u> many others have already gone broke.""",
        "6670_astounding_stories06_09_cummings_0058"
    ))
    blocks.append(_gen_table("short", "eng",
        "Original text: " + """Made open ports below of no necessity.""",
        "Edited text: " + """Made open <u><em><strong>large</strong></em></u> ports below of no necessity.""",
        "6671_insearchofmademoiselle_02_gibbs_0011"

    ))
    blocks.append(_gen_table("short", "eng",
        "Original text: " + """You are no longer in the midst of broken desolate wastes.""",
        "Edited text: " + """You are no longer in the <u><em><strong>middle</strong></em></u> midst of broken desolate wastes.""",
        "11697_actressinhighlife_01_bowen_0027"
    ))
   