import os
import replicate

os.environ['REPLICATE_API_TOKEN'] = "r8_5KNtdaDEHlVxBbeg52Fmjq2PGl2lOWd0wi3aU"


def create_photo(promt):
    output = replicate.run(
        "ai-forever/kandinsky-2:601eea49d49003e6ea75a11527209c4f510a93e2112c969d548fbb45b9c4f19f",
        input={"prompt": promt}
    )
    return (output)
