LETTERS = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
N = 52
def shift_text(text, shift):
       res = []

       for word in text:
              new_word = word[-shift % len(word):] + word[:-shift % len(word)]
              if '/' in new_word:
                     new_word = new_word[:-1] + '\n'
                     shift += 1
              res.append(new_word)

       return res


def decrypt_text(text, shift):
       res = []

       for word in text:
              new_word = []
              for letter in word:
                     if letter not in LETTERS:
                            new_word.append(letter)
                     else:
                            ind = LETTERS.index(letter)
                            new_ind = (ind + shift) % N
                            new_word.append(LETTERS[new_ind])

              new_word = ''.join(new_word)
              res.append(new_word)

       return ' '.join(res)


text = 'vujgvmCfb tj ufscfu ouib z/vhm ' \
       'jdjuFyqm jt fscfuu uibo jdju/jnqm ' \
       'fTjnqm tj scfuuf ibou fy/dpnqm yDpnqmf jt cfuufs boui dbufe/dpnqmj ' \
       'uGmb tj fuufsc ouib oftufe/ ' \
       'bstfTq jt uufscf uibo otf/ef uzSfbebcjmj vout/dp ' \
       'djbmTqf dbtft (ubsfo djbmtqf hifopv up csfbl ifu t/svmf ' \
       'ipvhiBmu zqsbdujdbmju fbutc uz/qvsj Fsspst tipvme wfsof qbtt foumz/tjm ' \
       'omfttV mjdjumzfyq odfe/tjmf ' \
       'Jo fui dfgb pg hvjuz-bncj gvtfsf fui ubujpoufnq up ftt/hv ' \
       'Uifsf vmetip fc pof.. boe sbcmzqsfgf zpom pof pvt..pcwj xbz pu pe ju/ ' \
       'Bmuipvhi uibu bzx bzn puo cf wjpvtpc bu jstug ttvomf sfzpv( i/Evud ' \
       'xOp tj scfuuf ibou /ofwfs ' \
       'uipvhiBm fsofw jt fopgu cfuufs boui iu++sjh x/op ' \
       'gJ ifu nfoubujpojnqmf tj eibs pu mbjo-fyq tju( b bec /jefb ' \
       'Jg fui foubujpojnqmfn jt fbtz up bjo-fyqm ju znb cf b hppe jefb/ ' \
       'bnftqbdftO bsf pof ipoljoh sfbuh efbj .. fu(tm pe psfn gp tf"uip'.split()

shift1 = 3
shift2 = N - 1
shifted_lines = shift_text(text, shift1)
decrypted_text = decrypt_text(shifted_lines, shift2)

print(decrypted_text)


