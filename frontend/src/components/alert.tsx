import { Alert } from '@mui/material';
import { CheckIcon } from 'lucide-react';

type Props = {
  handleCloseAlert: () => void;
  alertMessage: string;
};

export const AlertComponent = ({ handleCloseAlert, alertMessage }: Props) => {
  return (
    <Alert
      icon={<CheckIcon fontSize="inherit" style={{ color: '#01aa01' }} />}
      severity="success"
      onClose={handleCloseAlert}
      style={{
        position: 'fixed',
				width: '295px',
        bottom: '50px',
        left: '50%',
        transform: 'translateX(-50%)',
        zIndex: 1000,
        border: '1px solid #01aa01',
        color: '#01aa01',
        background: '#111d3a',
      }}>
      {alertMessage}
    </Alert>
  );
};
