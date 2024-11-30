import { Box, Button, FormControl, FormHelperText, TextField } from '@mui/material';
import React, { useState } from 'react';
import { useForm } from 'react-hook-form';
import { useNavigate } from 'react-router-dom';

interface SmsFormInput {
  sms: string;
}

export const FormSms: React.FC = () => {
  const {
    register,
    handleSubmit,
    setValue,
    formState: { errors },
  } = useForm<SmsFormInput>();
  const [sms, setSms] = useState('');
  const [isLoading, setIsLoading] = useState(false);

  const navigate = useNavigate();

  const handleInput = (event: React.ChangeEvent<HTMLInputElement>) => {
    const value = event.target.value.replace(/\D/g, '');
    if (value.length <= 4) {
      setSms(value);
      setValue('sms', value);
    }
  };

  const onSubmit = (data: SmsFormInput) => {
    console.log('Submitted SMS:', data.sms);

    setIsLoading(true);
    setTimeout(() => {
      navigate('/chats');
      setIsLoading(false);
    }, 1000);
  };

  const isButtonDisabled = sms.length !== 4;

  return (
    <div className="form">
      <div className="form__title">Авторизация</div>
      <Box
        className="form__block"
        onSubmit={handleSubmit(onSubmit)}
        component="form"
        sx={{ '& .MuiTextField-root': { width: '25ch' } }}
        autoComplete="off">
        <div className="form-inputs">
          <FormControl fullWidth error={!!errors.sms}>
            <div className="form__label">SMS-код</div>
            <TextField
              value={sms}
              {...register('sms', {
                required: 'SMS-код',
              })}
              onChange={handleInput}
              placeholder="XXXX"
              autoComplete="off"
              error={!!errors.sms}
              inputProps={{
                maxLength: 4,
                style: {
                  textAlign: 'center',
                  fontSize: '1.5rem',
                  letterSpacing: '15px',
                  marginLeft: '13px',
                },
              }}
              sx={{
                '& .MuiOutlinedInput-root': {
                  '& fieldset': {
                    borderColor: '#212d3a',
                    borderRadius: '8px',
                  },
                  '&:hover fieldset': {
                    borderColor: '#212d3a',
                  },
                  '&.Mui-focused fieldset': {
                    borderColor: '#212d3a',
                  },
                },
                '& .MuiInputBase-input': {
                  color: '#212d3a',
                  height: '2.2ch',
                },
                '& .MuiInputBase-input::placeholder': {
                  color: '#212d3a',
                  opacity: 0.8,
                  letterSpacing: '15px',
                  fontSize: '1.3rem',
                },
              }}
            />
            <FormHelperText style={{ marginLeft: '12px' }}>{errors.sms?.message}</FormHelperText>
          </FormControl>
        </div>
        <Button
          sx={{
            backgroundColor: isButtonDisabled ? 'gray' : '#212d3a',
            color: isButtonDisabled ? 'gray' : 'white',
            '&.Mui-disabled': {
              color: 'grey',
              cursor: 'not-allowed',
            },
            fontSize: '1rem',
            padding: '8px 30px',
            borderRadius: '8px',
          }}
          type="submit"
          style={{ marginTop: '35px' }}
          variant="contained"
          disabled={isButtonDisabled}>
          {isLoading ? 'Загрузка...' : 'Войти'}
        </Button>
      </Box>
    </div>
  );
};
