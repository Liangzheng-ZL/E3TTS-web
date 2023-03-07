"""
HTML generator for Section: Abstract.
"""

from dominate.tags import *
from templates.audios import audio_table, audio_grid
from dominate.util import raw


def section_abstract():
    # Compare with GuidedTTS 2 Audio Samples:
    h3("Abstract")
    p(
        """
        In recent years, text-to-speech (TTS) models have made great progress and received widespread applications. Recorded audio plays a critical role and is irreplaceable in our daily communication in spite of the high-fidelity speech produced by TTS models. It is of practical value to manipulate the recorded audio flexibly in many scenarios such as audio post-production. However, it is still challenging to "edit" the recording based on current TTS models given the diversity and variability lied in the realistic speech. In this paper, we extend the neural TTS model by incorporating the contextual spectrum and prosody features to construct a text-based speech editing system, which is named BEdit-TTS.  Our proposed model allows  deletion, insertion and replacement operations on the recording.  The objective and subjective evaluations on English and Chinese demonstrate the effectiveness of the proposed model and exhibit superior performance over several competitive baseline systems. 
        """,
        # br(),
        # br(),
        # """The following are 6 different renditions of the abstract by a DiffVoice model. Note that this model does not have any speaker input.""",
        # raw("""It samples <b>DIFF</b>erent <b>VOICE</b>s from the latent space."""),
        # _class="lead"
    )
    h3("Baseline models")
    p(
        """
        The implementations of baseline systems are based on the same FastSpeech 2 model.
        """,
        br(),
        raw("""<b>Baseline 1</b>: This system generates the complete speech audio from the edited text."""),
        br(),
        raw("""
        <b>Baseline 2</b>: This system generates only the shot speech segment with the input words of the modified region, then inserts the segment into the corresponding position of the original speech. 
        """),
        br(),
        raw("""
        <b>Baseline 3</b>: This system also generates a complete speech, but the shot speech segment corresponding to the modified region words is cut from the generation and inserted into the corresponding position of the original speech.
        """),
        br(),
    )
    # audio_grid(
    #     audio_files=[f"/diffvoice-web/samples/abstract/{name}.wav" for name in ["f_0", "f_1", "f_2", "m_0", "m_1", "m_2"]],
    #     width=3, control_width_px=300
    # )