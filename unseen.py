from dominate.tags import *
from dominate.util import raw
from templates.audios import audio_table, my_audio_table
from templates.spinspy import nav_spin


def section_replace_compare():
    h3("Reconstruction")
    p(
        [
            """In this section, we demonstrate BEdit-TTS's ability with the setting of unseen speaker. """,
        ], _class="lead"
    )
    blocks = []
    def _gen_table(length: str, language: str, o_text: str, e_text: str, name: str):
        return my_audio_table(
            o_text=o_text,
            e_text=e_text,
            audio_files=[
                f"./samples/unseen/{language}/{sys}/{name}.wav" for sys in (
                    "gt", "gt-vocoder","bedit-tts",
                )
            ],
            titles=[
                f"Original audio", "Vocoder", "BEdit-TTS"
            ],
            width=3, control_width_px=250
        )
    blocks.append(_gen_table("short", "eng",
        None,
        "Text: " + """<u><em><strong>They were</strong></em></u>old friends.""",
        "237_134500_000021_000001"
    ))

    blocks.append(_gen_table("short", "eng",
        None,
        "Text: " + """<u><em><strong>We are</strong></em></u> prostrated and worn out with fatigue.""",
        "260_123288_000032_000000"
    ))
    blocks.append(_gen_table("short", "eng",
        None, 
        "Text: " + """The <u><em><strong>milk is</strong></em></u> very good.""",
        "3729_6852_000039_000000"
    ))
    blocks.append(_gen_table("short", "eng",
        None, 
        "Text: " + """<u><em><strong>Approaching the dining table</strong></em></u> he carefully placed the article in the centre and removed the cloth.""",
        "4992_41806_000025_000001"

    ))
    blocks.append(_gen_table("short", "eng",
        None,
        "Text: " + """There was in that city a young cavalier about two and twenty years of age whom wealth high birth <u><em><strong>a wayward disposition</strong></em></u> inordinate indulgence and profligate companions impelled to do things which disgraced his rank.""",
        "5639000000"
    ))
    blocks.append(_gen_table("short", "chn",
        None,
        "Text: " + """<u><em><strong>我放弃这个想法。</strong></em></u>""",
        "SSB07490200"
    ))
    blocks.append(_gen_table("short", "chn",
        None, 
        "Text: " + """汽车厂商几乎承包<u><em><strong>了一半的</strong></em></u>面积。""",
        "SSB11350318"
    ))
    blocks.append(_gen_table("short", "chn",
        None, 
        "Text: " + """给<u><em><strong>我切换到</strong></em></u>东南卫视。""",
        "SSB08220185"
    ))
    blocks.append(_gen_table("short", "chn",
        None, 
        "Text: " + """整体定位和发展战略不会发<u><em><strong>生变化</strong></em></u>。""",
        "SSB12390151"
    ))
    blocks.append(_gen_table("short", "chn",
        None,
        "Text: " + """南京雨<u><em><strong>花台警方捣毁一诈</strong></em></u>骗团伙。""",
        "SSB12390412"
    ))


   