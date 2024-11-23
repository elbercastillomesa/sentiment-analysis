# Sentiment Analysis 

- [TikTok Video Comments](#Tiktok-POC)
- [YouTube Video Comments](#Youtube-POC)

---

## Tiktok-POC

- This is a **Proof of Concept (POC)**. Additional research is required to determine whether TikTok permits data extraction from its platform. Legal issues may arise before using this tool.
- TikTok's API and website structure are subject to change, which might require periodic adjustments to the scraper.
- The accuracy of sentiment analysis depends on the quality of the model and the nature of the comments.

### Steps:

1. **Extract Comments:**
   ```python
   comments_file = tiktok_scraper.get_comments(post_url)
   ```

2. **Load Comments for Analysis:**
   ```python
   comments_list = tiktok_scraper.load_comment_list(comments_file, 'text')
   df = create_dataframe(comments_list)
   ```

3. **Analyze General Sentiment:**
   ```python
   general_sentiment = evaluate_general_sentiment(df)
   print(general_sentiment)
   ```

4. **Generate Word Cloud:**
   ```python
   word_cloud = WordCloud(
       width=800, 
       height=600, 
       background_color='lavender',
       max_words=20, 
       stopwords=aditional_stopwords
   ).generate(df['comment'].str.cat(sep=' '))
   word_cloud.to_image()
   ```

---

## Youtube-POC

### Objective:

Develop a complete sentiment analysis application which reads a YouTube URL, fetch the comments and returns a simple report 
with a small bar graph. (This graph explains the proposed steps provided by [Tim](https://www.youtube.com/watch?v=lVbElR_HwXQ))

[![UML Diagram](./sentiment_uml.png)](#)

The model is trained using 

## Tools to Use:

- Python 3.x
- Django
- TensorFlow
- Kaggle [Dataset](https://www.youtube.com/watch?v=lVbElR_HwXQ)

------

## Dataset Selection:

## Clean Data:

## Model Training:

## Deploy/Use Model:

## API Development:

## Frontend Development:

## Initialize the APP (TBD)

- Install Docker and Docker CE/Docker Desktop if required.
- Clone the repository and "cd" into the folder.
- Run ```docker compose up ---build```
- Check the docker console for the React App URL (most probably [localhost](http://localhost/))
- 🔥🔥🔥 🖥️ 🔥🔥🔥

------

## Acknowledgments:

This project follows the directions from the following experts, thanks for sharing your knowledge:

- [Tech with Tim](https://www.youtube.com/watch?v=lVbElR_HwXQ)
- [TensorFlow ](https://github.com/cornflourblue)
- [CodeMate TV](https://www.youtube.com/watch?v=Tqnuhaaw738)
- [Rob Mulla](https://www.youtube.com/watch?v=QpzMWQvxXWk)
- [DiMathData](https://www.youtube.com/watch?v=X59oBuevKVA)