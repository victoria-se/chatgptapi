import openai
openai.api_key = ""

completion = openai.ChatCompletion.create(
    model = "gpt-3.5-turbo",
    messages = [
        # {
        #     "role": "user",
        #     "content" : "Before I ask you some songs that go well with a certain book,\
        #         I will give you a background knowledge on me. For artist, I like Parcels, Gloria Tells, Sufjan Stevens"
        #         #Justin Hurwitz, Exo, Dayglow.\
        #         #For genre, I like pop, indie pop, instrumental music",
        # },
        # {
        #     "role": "assistant",
        #     "content": "Thank you for letting me know. I will recommend music that would\
        #         go well with a book."
        # },
        # The Odyssey by Homer
        # The Works of Edgar Allan Poe, Volume 1 by Edgar Allan Poe
        # Don Quixote by Miguel de Cervantes
        # Pride and Prejudice by Jane Austen
        # A Week on the Concord and Merrimack Rivers by Henry David Thoreau 
        # Autobiography of Benjamin Franklin by Benjamin Franklin
        {
            "role": "user",
            "content" : "can you recommend 3 songs that go well with Autobiography of Benjamin Franklin by Benjamin Franklin\
                in json format aligning with spotify API usage",
        }

    ],
)

print(completion["choices"]) 
