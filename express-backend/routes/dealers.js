const express = require('express');
const router = express.Router();

// Dummy data for 10 dealers
const dealers = [
    { id: 1, name: 'Dealer One', state: 'Kansas', details: 'Details for Dealer One' },
    { id: 2, name: 'Dealer Two', state: 'Texas', details: 'Details for Dealer Two' },
    { id: 3, name: 'Dealer Three', state: 'Kansas', details: 'Details for Dealer Three' },
    { id: 4, name: 'Dealer Four', state: 'California', details: 'Details for Dealer Four' },
    { id: 5, name: 'Dealer Five', state: 'Florida', details: 'Details for Dealer Five' },
    { id: 6, name: 'Dealer Six', state: 'New York', details: 'Details for Dealer Six' },
    { id: 7, name: 'Dealer Seven', state: 'Illinois', details: 'Details for Dealer Seven' },
    { id: 8, name: 'Dealer Eight', state: 'Ohio', details: 'Details for Dealer Eight' },
    { id: 9, name: 'Dealer Nine', state: 'Georgia', details: 'Details for Dealer Nine' },
    { id: 10, name: 'Dealer Ten', state: 'Nevada', details: 'Details for Dealer Ten' }
];

// Get all dealers
router.get('/', (req, res) => {
    res.json(dealers);
});

// Get dealer by ID
router.get('/:id', (req, res) => {
    const dealer = dealers.find(d => d.id === parseInt(req.params.id));
    if (dealer) {
        res.json(dealer);
    } else {
        res.status(404).json({ error: 'Dealer not found' });
    }
});

// Get dealers by state
router.get('/state/:state', (req, res) => {
    const stateDealers = dealers.filter(d => d.state.toLowerCase() === req.params.state.toLowerCase());
    res.json(stateDealers);
});

module.exports = router;