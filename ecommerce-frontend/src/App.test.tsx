import { render, screen } from '@testing-library/react';
import App from './App';

test('renders dashboard heading after loading finishes', async () => {
  render(<App />);

  // Verify the loader appears first
  expect(screen.getByRole('progressbar')).toBeInTheDocument();

  // Wait for the heading to appear 
  const headingElement = await screen.findByRole('heading', { 
    level: 1, 
    name: /product management dashboard/i 
  }, { timeout: 2000 }); // Timeout if not found within 2 seconds

  expect(headingElement).toBeInTheDocument();
});