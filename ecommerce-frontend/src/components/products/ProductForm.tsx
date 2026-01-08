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
    <Dialog open={open} onClose={onClose} fullWidth maxWidth="sm">
        <DialogTitle>
            {product ? 'Edit Product' : 'Add Product'}
        </DialogTitle>
        <DialogContent>
            <TextField
                autoFocus
                margin='dense'
                label='Product Name'
                fullWidth
                variant='outlined'
                value={formData.name}
                onChange={(e) => setFormData({...formData, name: e.target.value})}
                required
                sx={{ marginBottom: 2 }}
            />
            <TextField
                margin='dense'
                label='Price'
                type='number'
                fullWidth
                variant='outlined'
                value={formData.price}
                onChange={(e) => setFormData({...formData, price: parseFloat(e.target.value)})}
                required
                sx={{ marginBottom: 2 }}
            />
            <TextField
                margin='dense'
                label='Description'
                fullWidth
                variant='outlined'
                multiline
                rows={4}
                value={formData.description}
                onChange={(e) => setFormData({...formData, description: e.target.value})}
                required
                sx={{ marginBottom: 2 }}
            />
            <TextField
                select
                margin='dense'
                label='Category'
                fullWidth
                variant='outlined'
                value={formData.category}
                onChange={(e) => setFormData({...formData, category: e.target.value})}
                required
                sx={{ marginBottom: 2 }}
            >
                {categories.map((category) => (
                    <MenuItem key={category} value={category}>
                        {category}
                    </MenuItem>
                ))}
            </TextField>
        </DialogContent>
        <DialogActions>
            <Button onClick={onClose} color='secondary'>
                Cancel
            </Button>
            <Button onClick={handleSubmit} color='primary'>
                {product ? 'Update' : 'Create'}
            </Button>
        </DialogActions>
    </Dialog>
  );
};

export default ProductForm;