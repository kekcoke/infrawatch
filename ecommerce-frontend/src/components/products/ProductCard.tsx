// src/components/products/ProductCard.tsx
import React from 'react';
import { Box, Button, Card, CardActions, CardContent, Chip, Typography } from '@mui/material';
import { Product } from '../../types/Product';

interface ProductCardProps {
    product: Product;
    onEdit: (product: Product) => void;
    onDelete: (productId: number) => void;
}
