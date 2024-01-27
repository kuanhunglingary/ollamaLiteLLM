import ollama

stream = ollama.chat(
    model="mistral",
    messages=[{"role": "user", "content": "Tell me a ghost story"}],
    stream=True,
)

for chunk in stream:
    print(chunk["message"]["content"], end="", flush=True)


# Once upon a time, in the small rural village of Hollow Creek, nestled between rolling hills and dense forests, there stood an old, grand mansion. This once magnificent home was known as Ravenwood Manor. It had been passed down through generations of the wealthy Ravenwood family for centuries. But as the years went by and fortune faded, so too did the manor, falling into disrepair and decay.

# The villagers spoke in hushed whispers about the manor, warning each other to never go near it after dark. They told tales of strange noises and eerie apparitions that roamed the halls, seeking vengeance for some long-forgotten wrong. Many claimed to have seen the ghostly figure of Lady Ravenwood, clad in a tattered white gown, weeping by her shattered mirror. Others spoke of the spectral sound of a grand ball being held within its walls, where the laughter and music could be heard echoing through the forest.

# One fateful night, as the moon hung heavy and full in the sky, a group of thrill-seeking teenagers decided to venture into the manor to uncover its secrets. Armed with flashlights and cameras, they explored the dark corridors, their laughter bouncing off the damp walls. But as they delved deeper into the manor, the laughter subsided, replaced by a feeling of unease.

# Suddenly, they heard it – a soft, haunting melody, drifting through the halls like a ghostly wisp of mist. The teenagers followed the music, their hearts pounding in their chests as they entered a grand ballroom. There, bathed in the pale glow of the moonlight streaming through the shattered windows, stood Lady Ravenwood. She turned to face them, her eyes glowing with an otherworldly light, and spoke in a voice that seemed to come from the very walls themselves.

# "You have dared to disturb my rest," she whispered. "Now you shall bear witness to the consequences of your folly." And with that, the ghostly figure raised her spectral hand, and the manor began to shake and tremble as if awakening from a long slumber. The teenagers fled in terror, but they knew they would never forget the sight of Lady Ravenwood and the haunting melody that lingered in their minds forevermore.

# And so it was that the legend of Ravenwood Manor continued to grow, its ghostly inhabitants seeking vengeance upon those who dared to disturb their eternal rest. And the villagers whispered amongst themselves, warning each other to never go near the manor after dark, lest they too fall victim to its spectral haunting.%
