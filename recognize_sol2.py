# produces graph only [fails to find output mappings]
from nltk.nltk_contrib.fst.fst import *

class ChineseEnglishFST(FST):
    def check(self, input_str):
        current_state = self.initial_state
        output_sequence = []

        for symbol in input_str.split():
            arcs = self.transitions.get((current_state, symbol), [])
            if not arcs:
                print(f"No transition for symbol '{symbol}' at state {current_state}")
                break

            arc = arcs[0]  # Assume a non-deterministic FST, take the first arc
            current_state = arc.nextstate
            output_sequence.append(arc.olabel)

            print(f"Transition: {current_state} --({symbol}/{arc.ilabel}:{arc.olabel})--> {arc.nextstate}")

        if current_state in self.states:
            print(f"Reached final state: {current_state}")
            return output_sequence
        else:
            print(f"Failed to reach final state. Current state: {current_state}")
            return None
        
def generate_mappings():
    pinyin_mappings = {}

    # Add mappings for individual Pinyin components
    individual_mappings = {
        "ga": "cur",
        "li": ["ry", "rie"],
        "ka": ["ca"],
        "lu": ["lo"],
       "wei": ["vi"],
        "ta": ["ta"],
      "ming": ["min"],
       "fei": ["fee"],
       "lei": ["la"],
       "she": ["ser"],
       }
    
    for key, value in individual_mappings.items():
        if isinstance(value, list):
            for i, sub_value in enumerate(value):
                pinyin_mappings[f"{key}_{i}"] = sub_value
        else:
            pinyin_mappings[key] = value

    # Add mappings for combined Pinyin
    combined_mappings = {
        "ga li": "cur ry",
        "ka lu li": "ca lo rie",
        "wei ta ming":"vi ta min",
        "ka fei": "cof fee",
        "lei she": "la ser",
        "beng dai": "band age",
        "amo ni ya": "am mo nia",
        "asi pi lin": "as pi rin",
        "bei guo": "ba gel",
        "ban zhuo qin": "ban jo",
        "ba lei": "bal let",
        "bu lu si": "blu es",
        "ba shi": "b us",
        "ka fei yin": "caf fei ne",
        "ka tong": "car toon",
        "zhi shi": "che ese",
        "qiao ke li": "cho co late",
        "qu qi": "coo kie",
        "sha fa": "so fa",
        "tu si": "toa st",
        "de lu feng": "te le phone",
        "shi duo pi li": "straw ber ry",
        "sang na": "heal th",
        "ma ke bei": "m ug",
        "mai ke feng": "mi cro phone",
        "ma sha ji": "mas sage",
        "ning meng": "le mon",
        "jia ke": "jac ket",
        "su ke da": "scoo ter",
        "xiang bo": "sham poo",
        "ji ta": "gui tar",
        "ha ni": "ho ney",
        "ni long": "ny lon",
        "di shi": "ta xi",
        "yu jia": "yo ga"
    }
    pinyin_mappings.update(combined_mappings)

    return pinyin_mappings

def construct_fst(pinyin_mappings):
    fst = ChineseEnglishFST("chinese-english")

    # Adding states
    for i in range(len(pinyin_mappings) * 2 + 1):
        fst.add_state(str(i))

    # Initial State
    fst.initial_state = "0"

    # Final States
    for i in range(1, len(pinyin_mappings) * 2 + 1, 2):
        fst.set_final(str(i))

    # Adding arcs
    current_state = 0
    for pinyin, transl in pinyin_mappings.items():
        current_state += 1
        fst.add_arc(str(current_state - 1), str(current_state), "", pinyin)  # Fixed this line

        if isinstance(transl, list):
            for i, sub_transl in enumerate(transl):
                fst.add_arc(str(current_state), str(current_state + 1), "", f"{pinyin}_{i}", sub_transl)
                current_state += 1
        else:
            fst.add_arc(str(current_state), str(current_state + 1), "", "", transl)  # Fixed this line
            current_state += 1

    return fst

if __name__ == "__main__":
    mappings = generate_mappings()
    fst_instance = construct_fst(mappings)

    # Exporting to file
    output_file_path = "Chinglish-trans.dat"
    with open(output_file_path, "w") as file:
        for pinyin, transl in mappings.items():
            try:
                if " " in pinyin:
                    # Combined Pinyin form
                    combined_output = fst_instance.check(pinyin)
                    if combined_output:
                        file.write(f"{pinyin:50} {'-->':10} {' '.join(map(str, combined_output))}\n")
                else:
                    # Individual Pinyin form
                    output = fst_instance.check(pinyin)
                    if output:
                        file.write(f"{pinyin:50} {'-->':10} {' '.join(map(str, output))}\n")
                    else:
                        print(f"Failed to find: {pinyin}")
            except Exception as e:
                print(f"Failed to find: {pinyin}")

    # Show FST in Tkinter window
    FSTDisplay(fst_instance).cf.mainloop()