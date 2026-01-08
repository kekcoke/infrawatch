import { render, screen } from '@testing-library/react';
import App from './App';
import axios from 'axios';

jest.mock('axios');
const mockedAxios = axios as jest.Mocked<typeof axios>;

test('renders dashboard heading after loading finishes', async () => {
  mockedAxios.get.mockResolvedValue({
    data: [{ id: 1, name: 'Test Product' }]
  });
  
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