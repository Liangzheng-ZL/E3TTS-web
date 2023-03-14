from dominate.tags import *
from dominate.util import raw
from templates.audios import audio_table, my_audio_table, length_audio_table
from templates.spinspy import nav_spin


def section_length_compare():
    h3("Insertion Length Robustness")
    h4("Middle")
    blocks = []
    def _gen_table(length: str, language: str, o_text: str, mide_text: str, longe_text: str, name: str):
        return length_audio_table(
            o_text=o_text,
            mide_text=mide_text,
            longe_text=longe_text,
            audio_files=[
                f"./samples/length/{sys}/{name}.wav" for sys in (
                    "gt", "mid", "long", "full"
                )
            ],
            titles=[
                f"Original audio", "Middle", "Long", "Full Sentence"
            ],
            width=4, control_width_px=250
        )

    blocks.append(_gen_table("mid", "eng",
        "Original text: " + """The pleasant season did my heart employ.""",
        "Edited text (middle): " + """The pleasant <u><em><strong>spring summer autumn and winter</strong></em></u> season did my heart employ.""",
        "Edited text (long): " + """The pleasant <u><em><strong>spring summer autumn winter spring summer autumn and winter</strong></em></u> season did my heart employ.""",
        "11697_actressinhighlife_01_bowen_0001"
    ))
    blocks.append(_gen_table("mid", "eng",
        "Original text: " + """And nothing but the truth.""",
        "Edited text (middle): " + """And <u><em><strong>tell me and tell him</strong></em></u> nothing but the truth.""",
        "Edited text (long): " + """And <u><em><strong>tell me, tell him, tell her, tell you</strong></em></u> nothing but the truth.""",
        "12787_bigbluesoldier_01_hill_0003"
    ))
    blocks.append(_gen_table("mid", "eng",
        "Original text: " + """What if my nephew Dick should be needing one.""",
        "Edited text (middle): " + """What if my nephew Dick <u><em><strong>comes back to his room</strong></em></u> should be needing one.""",
        "Edited text (long): " + """What if my nephew Dick <u><em><strong>coming back to his room and doing homework</strong></em></u> should be needing one.""",
        "12787_bigbluesoldier_01_hill_0018"

    ))
    blocks.append(_gen_table("mid", "eng",
        "Original text: " + """And most people had begun to use pink and blue wool on their needles.""",
        "Edited text (middle): " + """And most <u><em><strong>sensible and beautiful</strong></em></u> people had begun to use pink and blue wool on their needles.""",
        "Edited text (long): " + """And most <u><em><strong>sensible and beautiful and sensible and beautiful</strong></em></u> people had begun to use pink and blue wool on their needles.""",
        "12787_bigbluesoldier_01_hill_0021"
    ))
    # blocks.append(_gen_table("mid", "eng",
    #     "Original text: " + """Their children bullied.""",
    #     "Edited text: " + """Their children <u><em><strong>more deeply into its philosophy</strong></em></u> bullied.""",
    #     "12787_bigbluesoldier_01_hill_0042"
    # ))
    