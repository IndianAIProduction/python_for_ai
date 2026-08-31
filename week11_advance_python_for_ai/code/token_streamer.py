import time

HISTORY_OF_INDIA = """India has one of the world's oldest and most diverse civilizations. Its history spans thousands of years, from the Indus Valley Civilization to the modern Republic of India.

1. Ancient India — c. 2500 BCE–600 BCE
Indus Valley Civilization (c. 2500–1900 BCE): One of the world's earliest urban civilizations, centered around cities such as Harappa and Mohenjo-daro. People built planned cities, drainage systems, and engaged in long-distance trade.
Vedic Period (c. 1500–600 BCE): Indo-Aryan-speaking communities developed across northern India. The Vedas were composed, and early Hindu religious and social traditions developed.
By the later Vedic period, larger kingdoms and states emerged.
2. Mahajanapadas and the rise of religions — c. 600–300 BCE

Around the 6th century BCE, northern India contained several major kingdoms known as the Mahajanapadas.

Two major religious traditions emerged:

Buddhism, founded by Gautama Buddha.
Jainism, associated particularly with Mahavira.

The kingdom of Magadha became increasingly powerful.

3. Mauryan Empire — c. 322–185 BCE

Chandragupta Maurya established the Mauryan Empire, creating one of the first large empires to unite much of the Indian subcontinent.

His grandson, Ashoka, became one of India's most famous rulers. After the devastating Kalinga War, he embraced Buddhism and promoted principles of nonviolence and ethical governance.

4. Classical India — c. 300–750 CE

Several powerful kingdoms flourished.

The Gupta Empire (roughly 4th–6th centuries CE) is often called a "Golden Age" because of major developments in:

Mathematics and astronomy
Sanskrit literature
Art and architecture
Medicine
Philosophy

The mathematician Aryabhata made important contributions to astronomy and mathematics.

Southern India also saw powerful kingdoms and flourishing trade with Southeast Asia.

5. Medieval India — c. 750–1526

India became politically fragmented among numerous kingdoms.

Important powers included:

Cholas in southern India
Rajput kingdoms in northern and western India
Pala and Pratihara dynasties
Various Deccan kingdoms

From the 12th century onward, several Muslim dynasties established themselves in northern India.

The Delhi Sultanate (1206–1526) ruled large parts of northern India at different times. This period saw substantial interaction and blending among Indian, Persian, Central Asian and Islamic cultural traditions.

6. Mughal Empire — 1526–1857

Babur defeated Ibrahim Lodi at the First Battle of Panipat in 1526 and established the Mughal Empire.

Important Mughal rulers included:

Akbar — expanded the empire and pursued policies of political and religious accommodation.
Jahangir
Shah Jahan — commissioned the Taj Mahal.
Aurangzeb — expanded Mughal territory to its greatest extent, although the empire faced increasing challenges.

The Mughal period had an enormous influence on Indian architecture, art, language, cuisine and administration.

7. European expansion and British rule — 1600s–1947

European trading powers established settlements in India, including the Portuguese, Dutch, French and British.

The British East India Company gradually transformed itself from a trading organization into a major political power.

After the Battle of Plassey (1757), British influence expanded dramatically.

The Indian Rebellion of 1857 was a major uprising against Company rule. After it, the British government took direct control of India in 1858, beginning the period commonly called the British Raj.

8. Indian independence movement — late 19th century–1947

Indian political movements increasingly demanded greater self-government and eventually independence.

Important figures included:

Mahatma Gandhi, who promoted mass nonviolent resistance.
Jawaharlal Nehru
Sardar Vallabhbhai Patel
Subhas Chandra Bose
B. R. Ambedkar, a central figure in India's constitutional development and the struggle against caste discrimination.

The Indian National Congress became a major force in the independence movement.

India became independent from British rule on 15 August 1947.

Independence was accompanied by the Partition of British India, which created India and Pakistan and resulted in enormous population movements and communal violence.

9. Republic of India — 1950 to today

India adopted its Constitution on 26 November 1949, and it came into effect on 26 January 1950, when India became a republic.

Jawaharlal Nehru became the country's first prime minister.

Since independence, India has experienced:

Democratic elections and changes of government
Rapid population and economic growth
The Green Revolution and major agricultural transformation
Industrialization and technological development
Economic liberalization beginning in 1991
Major growth in information technology and services
Increasing global political and economic influence

Today, India is a federal democratic republic and one of the world's largest economies and most populous countries.

A very short timeline

Indus Valley → Vedic Period → Mahajanapadas → Mauryas → Guptas → Regional Kingdoms → Delhi Sultanate → Mughals → British Rule → Independence & Partition (1947) → Republic of India (1950–present)

If you're learning this for school or general knowledge, the most useful next step is to study it as Ancient India → Medieval India → Modern India, with the major rulers, wars, religions, and cultural developments in each period."""


def stream_responce(text):
    for word in text.split():
        time.sleep(0.025)
        yield word


gen_streamer = stream_responce(HISTORY_OF_INDIA)
for word in gen_streamer:
    print(word, end = " ", flush=True)