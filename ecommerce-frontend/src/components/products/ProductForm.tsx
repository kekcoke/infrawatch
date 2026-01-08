// src/components/products/ProductForm.tsx
import React, { useState, useEffect } from 'react';
import {
  Dialog,
  DialogTitle,
  DialogContent,
  DialogActions,
  TextField,
  Button,
  FormControlLabel,
  Switch,
  MenuItem,
} from '@mui/material';
import { Product, ProductFormData } from '../../types/Product';

interface ProductFormProps {
  open: boolean;
  product: Product | null;
  onSave: (data: ProductFormData) => void;
  onClose: () => void;
}

const categories = ['Electronics', 'Books', 'Clothing', 'Home', 'Sports'];

const ProductForm: React.FC<ProductFormProps> = ({ open, product, onSave, onClose }) => {
  const [formData, setFormData] = useState<ProductFormData>({
    name: '',
    price: 0,
    description: '',
    category: categories[0],
    inStock: true,
  });

  useEffect(() => {
    if (product) {
      setFormData({
        name: product.name,
        price: product.price,
        description: product.description,
        category: product.category,
        inStock: product.inStock,
      });
    } else {
      setFormData({
        name: '',
        price: 0,
        description: '',
        category: categories[0],
        inStock: true,
      });
    }
  }, [product, open])

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    onSave(formData);
  };

  return (
    <Dialog open={open} onClose={onClose} fullWidth maxWidth="sm"></Dialog>
  );
};