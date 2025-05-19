const express = require('express');
const app = express();
const dealersRouter = require('./routes/dealers');
const reviewsRouter = require('./routes/reviews');

app.use(express.json());
app.use('/dealers', dealersRouter);
app.use('/reviews', reviewsRouter);

// Sentiment analyzer endpoint
app.get('/sentiment', (req, res) => {
    const text = req.query.text || '';
    const sentiment = text.toLowerCase().includes('good') ? 'positive' : 'negative';
    res.json({ text, sentiment });
});

app.get('/', (req, res) => {
    res.send('Express Backend Root');
});

const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
    console.log(`Server running on port ${PORT}`);
});