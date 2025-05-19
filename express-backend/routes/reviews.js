const express = require('express');
const router = express.Router();

// Dummy data for reviews
const reviews = [
    { id: 1, dealerId: 1, review: 'Great service!', reviewer: 'Alice' },
    { id: 2, dealerId: 1, review: 'Good prices.', reviewer: 'Bob' },
    { id: 3, dealerId: 2, review: 'Not satisfied.', reviewer: 'Charlie' }
];

// Get reviews for a dealer
router.get('/:dealerId', function(req, res) {
    const dealerReviews = reviews.filter(r => r.dealerId === parseInt(req.params.dealerId));
    res.json(dealerReviews);
});

module.exports = router;