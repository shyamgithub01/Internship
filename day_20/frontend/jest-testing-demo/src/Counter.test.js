import { render, screen, fireEvent } from '@testing-library/react';
import Counter from './counter';

test('initial count is 0', () => {
  render(<Counter />);
  const countText = screen.getByTestId('count');
  expect(countText).toHaveTextContent('Count: 0');
});

test('increments count on button click', () => {
  render(<Counter />);
  const button = screen.getByText('Increment');
  fireEvent.click(button);
  const countText = screen.getByTestId('count');
  expect(countText).toHaveTextContent('Count: 1');
});
