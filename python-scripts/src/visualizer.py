from wordcloud import WordCloud
import matplotlib.pyplot as plt

def generate_word_cloud(word_counts, path_save, maxwords= 10):
    """Generación del diagrama a mostrar."""
    
    wc = WordCloud(width=800, height=400, background_color='white', max_words=maxwords)
    wc.generate_from_frequencies(word_counts)

    plt.figure(figsize=(10, 5))
    plt.imshow(wc)
    plt.axis('off')
    # plt.show()
    plt.savefig(f"{path_save}/abstract_keywords")
