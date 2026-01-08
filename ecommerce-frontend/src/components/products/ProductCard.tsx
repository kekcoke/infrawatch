// src/components/products/ProductCard.tsx
import React from 'react';
import { Box, Button, Card, CardActions, CardContent, Chip, Typography } from '@mui/material';
import { Product } from '../../types/Product';

interface ProductCardProps {
    product: Product;
    onEdit: (product: Product) => void;
    onDelete: (productId: number) => void;
}

const ProductCard: React.FC<ProductCardProps> = ({ product, onEdit, onDelete }) => {
    return (
        <Card sx={{ maxWidth: 345, margin: 1 }}>
            <CardContent>
            </CardContent>
        </Card> 
    );
};

export default ProductCard;