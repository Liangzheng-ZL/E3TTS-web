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
            """Each sample has 5 audios, of which are synthesized audios from baseline and proposed systems. """,
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
    blocks.append(_gen_table("short", "chn",
        "Original text: " + """梁家仁出演的电视剧有什么。""",
        "Edited text: " + """梁家仁<u><em><strong>曾经</strong></em></u>出演的电视剧有什么。""",
        "SSB00180003"
    ))
    blocks.append(_gen_table("short", "chn",
        "Original text: " + """来一首故乡。""",
        "Edited text: " + """来一首<u><em><strong>关于</strong></em></u>故乡。""",
        "SSB01120400"
    ))
    blocks.append(_gen_table("short", "chn",
        "Original text: " + """又被电梯外门夹住头和身子。""",
        "Edited text: " + """又被<u><em><strong>突然关闭的</strong></em></u>电梯外门夹住头和身子。""",
        "SSB07370462"
    ))
    blocks.append(_gen_table("short", "chn",
        "Original text: " + """河南平顶山化工厂氨气泄漏小孩儿咳血动物瘫倒。""",
        "Edited text: " + """河南平顶山化工厂<u><em><strong>发生</strong></em></u>氨气泄漏小孩儿咳血动物瘫倒。""",
        "SSB04270111"
    ))
    blocks.append(_gen_table("short", "chn",
        "Original text: " + """之后将学校告上了法庭。""",
        "Edited text: " + """之后将<u><em><strong>自己的</strong></em></u>学校告上了法庭。""",
        "SSB12180020"
    ))
   