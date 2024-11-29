import { Route, Routes } from 'react-router-dom';
import { ChatList } from './pages';
import './sass/app.scss';

export const App = () => {
  return (
    <Routes>
      <Route path="/chats" element={<ChatList />} />
    </Routes>
  );
};
