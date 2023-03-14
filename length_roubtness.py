from dominate.tags import *
from dominate.util import raw
from templates.audios import audio_table, my_audio_table
from templates.spinspy import nav_spin


def section_replace_compare():
    h3("Insertion Length Robustness")
    h4("Middle")
    blocks = []
    def _gen_table(length: str, language: str, o_text: str, e_text: str, name: str):
        return my_audio_table(
            o_text=o_text,
            e_text=e_text,
            audio_files=[
                f"./samples/length/{sys}/{name}.wav" for sys in (
                    "gt", "mid"
                )
            ],
            titles=[
                f"Original audio", "Middle"
            ],
            width=2, control_width_px=250
        )

    blocks.append(_gen_table("short", "eng",
        "Original text: " + """Many others have already gone broke.""",
        "Edited text: " + """<u><em><strong>Some</strong></em></u> others have already gone broke.""",
        "6670_astounding_stories06_09_cummings_0058"
    ))
    blocks.append(_gen_table("short", "eng",
        "Original text: " + """And upon them were set sails patterned after the wonderful new invention of master fletcher of rye.
""",
        "Edited text: " + """And upon them were set sails patterned after the wonderful new invention of <u><em><strong>inventor</strong></em></u> fletcher of rye.
""",
        "6671_insearchofmademoiselle_02_gibbs_0019"
    ))
    blocks.append(_gen_table("short", "eng",
        "Original text: " + """But I stood over him until he had done his work thoroughly.""",
        "Edited text: " + """But I stood over him until he had done his <u><em><strong>book</strong></em></u> thoroughly.""",
        "11614_barontrump_03_lockwood_0001"

    ))
    blocks.append(_gen_table("short", "eng",
        "Original text: " + """My old remembrances went from me wholly and all the ways of men so vain and melancholy.""",
        "Edited text: " + """My old remembrances went from me <u><em><strong>partly</strong></em></u> and all the ways of men so vain and melancholy.""",
        "11697_actressinhighlife_01_bowen_0002"
    ))

   