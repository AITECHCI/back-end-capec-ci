const jwt = require('jsonwebtoken');

const authMiddleware = (req, res, next) => {
    // Récupérer le token depuis l'en-tête Authorization
    const token = req.header('Authorization')?.replace('Bearer ', '');

    if (!token) {
        return res.status(401).json({ message: 'Accès refusé. Token manquant.' });
    }

    try {
        // Vérifier le token
        const decoded = jwt.verify(token, process.env.JWT_SECRET);
        req.userId = decoded.userId; // Ajouter l'ID utilisateur à la requête
        next();
    } catch (err) {
        res.status(400).json({ message: 'Token invalide.' });
    }
};

module.exports = authMiddleware;