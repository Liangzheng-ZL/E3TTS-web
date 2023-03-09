"""
HTML generator for Section: Comparison with GuidedTTS 2.
"""

from dominate.tags import *
from dominate.util import raw
from templates.audios import audio_table, my_audio_table
from templates.spinspy import nav_spin


def section_delete_compare():
    h3("Deletion")
    p(
        """
        The deletion operation of the BEdit-TTS can be operated in two fashions. 
        """,
        br(),
        raw("""<b>delete-1</b>: The first is to simply delete the corresponding Mel-spectrogram features and fed them to vocoder for audio generation. """),
        br(),
        raw("""
        <b>delete-2</b>: The second is the change the deletion operation as a replacement operation, by deleting the selected words and one more neighboring word, and then replace to that word, to fulfill the deletion operation. 
        """),
        br(),
    )
    blocks = []
    def _gen_table( language: str, o_text: str, e_text: str, name: str):
        return my_audio_table(
            o_text=o_text,
            e_text=e_text,
            audio_files=[
                f"/bedit_web/samples/delete/{language}/{sys}/{name}.wav" for sys in (
                    "gt", "bedit-1", "bedit-2",
                )
            ],
            titles=[
                f"Original audio", "BEdit-TTS delete-1", "BEdit-TTS delete-2"
            ],
            width=3, control_width_px=250
        )
    blocks.append(_gen_table("eng",
        None,
        "Edited text: " + """And <del>still</del> spoke of her nephew dick with bated breath and a sigh.""",
        "12787_bigbluesoldier_01_hill_0025"
    ))

    blocks.append(_gen_table( "eng",
        None,
        "Edited text: " + """Or whatever was the <del>present</del> task.""",
        "92_auntcretesemancipation_01_hill_0039"
    ))
    blocks.append(_gen_table( "eng",
        None,
        "Edited text: " + """But I stood over him until he had done his <del>work</del> thoroughly.
""",
        "11614_barontrump_03_lockwood_0001."
    ))
    blocks.append(_gen_table( "eng",
        None,
        "Edited text: " + """I should simply <del>have</del> become a luntic.""",
        "11614_barontrump_03_lockwood_0053"

    ))
    blocks.append(_gen_table( "eng",
        None,
        "Edited text: " + """ And most people had begun to use <del>pink</del> and blue wool on their needles.""",
        "12787_bigbluesoldier_01_hill_0021"
    ))
   