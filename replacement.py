from dominate.tags import *
from dominate.util import raw
from templates.audios import audio_table, my_audio_table
from templates.spinspy import nav_spin


def section_replace_compare():
    h3("Replacement")
    p(
        [
            """Each sample has 5 audios, of which are synthesized audios from baseline and proposed systems. """,
        ], _class="lead"
    )
    blocks = []
    def _gen_table(length: str, language: str, o_text: str, e_text: str, name: str):
        return my_audio_table(
            o_text=o_text,
            e_text=e_text,
            audio_files=[
                f"./samples/replace/{language}/{length}/{sys}/{name}.wav" for sys in (
                    "gt", "baseline1", "baseline2", "baseline3", "bedit-tts",
                )
            ],
            titles=[
                f"Original audio", "Baseline 1", "Baseline 2", "Baseline 3", "BEdit-TTS"
            ],
            width=5, control_width_px=250
        )
    blocks.append(_gen_table("short", "eng",
        "Original text: " + """Or whatever was the present task.""",
        "Edited text: " + """Or whatever was the <u><em><strong>current</strong></em></u> task.""",
        "92_auntcretesemancipation_01_hill_0039"
    ))

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
    blocks.append(_gen_table("short", "chn",
        "Original text: " + """星期六对吧。""",
        "Edited text: " + """星期<u><em><strong>一和星期二</strong></em></u>对吧。""",
        "SSB00180405"
    ))
    blocks.append(_gen_table("short", "chn",
        "Original text: " + """珍珠湖。""",
        "Edited text: " + """<u><em><strong>涵泽</strong></em></u>湖。""",
        "SSB00330447"
    ))
    blocks.append(_gen_table("short", "chn",
        "Original text: " + """安徽六岁女童被伤案告破女童母亲及同居男子被拘。""",
        "Edited text: " + """安徽六岁女童被伤案告破<u><em><strong>犯罪嫌疑人</strong></em></u>被拘。""",
        "SSB00730202"
    ))
    blocks.append(_gen_table("short", "chn",
        "Original text: " + """这标志着网络安全已经上升为国家的重要战略。""",
        "Edited text: " + """这标志着<u><em><strong>环境保护</strong></em></u>已经上升为国家的重要战略。""",
        "SSB07860324"
    ))
    blocks.append(_gen_table("short", "chn",
        "Original text: " + """陈晓东也因为女有了女儿变得更加温暖。""",
        "Edited text: " + """陈晓东也因为<u><em><strong>女儿结婚</strong></em></u>变得更加温暖。""",
        "SSB19390218"
    ))


   