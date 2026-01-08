// src/components/products/ProductList.tsx
import React, { useEffect, useState } from 'react';
import { Add as AddIcon } from '@mui/icons-material';
import { Alert, Box, Button, CircularProgress, Container, Typography } from '@mui/material';
import Grid from '@mui/material/Grid';
import { productService } from '../../services/api';
import { Product, ProductFormData } from '../../types/Product';
import ProductCard from './ProductCard';
import ProductForm from './ProductForm';

const ProductList: React.FC = () => {
    const [products, setProducts] = useState<Product[]>([]);
    const [loading, setLoading] = useState<boolean>(true);
    const [error, setError] = useState<string | null>(null);
    const [showForm, setShowForm] = useState<boolean>(false);
    const [editingProduct, setEditingProduct] = useState<Product | null>(null);

    useEffect(() => {
        loadProducts();
    }, []);

    const loadProducts = async () => {
        try {
            setLoading(true);
            const data = await productService.getAllProducts();
            setProducts(data);
            setError(null);
    } catch (err) {
        setError('Failed to load products. Ensure the backend server is running.');
        // Mock data in the interim
        setProducts([
            {
                id: 1,
                name: 'Sample Product',
                price: 29.99,
                description: 'This is a sample product for development',
                category: 'Electronics',
                inStock: true,
                createdAt: new Date().toISOString(),
                updatedAt: new Date().toISOString(),
            },
        ]);
    } finally {
      setLoading(false);
    }
  };

  const handleSaveProduct = async (data: ProductFormData) => {
    try {
      if (editingProduct) {
        await productService.updateProduct(editingProduct.id, data);
      } else {
        await productService.createProduct(data);
      }

      await loadProducts();
      setShowForm(false);
      setEditingProduct(null);
    } catch (err) {
      setError('Failed to save product. Please try again.');
    }
    };

      const handleEditProduct = (product: Product) => {
    setEditingProduct(product);
    setShowForm(true);
  };

  const handleDeleteProduct = async (id: number) => {
    try {
      await productService.deleteProduct(id);
      await loadProducts();
    } catch (err) {
      setError('Failed to delete product');
    }
  };

  if (loading) {
    return (
      <Box display="flex" justifyContent="center" mt={4}>
        <CircularProgress />
      </Box>
    );
  }

  return (
    <Container>
      <Box sx={{ my: 4 }}>
        <Typography variant="h4" component="h1" gutterBottom>
          Product Management Dashboard
        </Typography>
        
        {error && (
          <Alert severity="error" sx={{ mb: 2 }}>
            {error}
          </Alert>
        )}

        <Button
          variant="contained"
          startIcon={<AddIcon />}
          onClick={() => setShowForm(true)}
          sx={{ mb: 3 }}
        >
          Add Product
        </Button>

        <Grid container spacing={3}>
          {products.map((product) => (
            <Grid item xs={12} sm={6} md={4} key={product.id}>
              <ProductCard
                product={product}
                onEdit={handleEditProduct}
                onDelete={handleDeleteProduct}
              />
            </Grid>
          ))}
        </Grid>

        <ProductForm
          open={showForm}
          product={editingProduct}
          onSave={handleSaveProduct}
          onClose={() => {
            setShowForm(false);
            setEditingProduct(null);
          }}
        />
      </Box>
    </Container>
  );
};

export default ProductList;