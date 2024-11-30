import HighlightOffIcon from '@mui/icons-material/HighlightOff';
import { Box, Button, FormControl, FormHelperText, TextField } from '@mui/material';
import React, { useRef, useState } from 'react';
import { useForm } from 'react-hook-form';
import { useNavigate } from 'react-router-dom';

interface PhoneFormInput {
  phone: string;
}

export const FormPhone: React.FC = () => {
  const {
    register,
    handleSubmit,
    setValue,
    formState: { errors },
  } = useForm<PhoneFormInput>();
  const [phone, setPhone] = useState('+7');
  const [isLoading, setIsLoading] = useState(false);
  const [operator, setOperator] = useState<number>();

  const navigate = useNavigate();
  const inputRef = useRef<HTMLInputElement | null>(null);

  const handleInput = (event: React.ChangeEvent<HTMLInputElement>) => {
    let value = event.target.value.replace(/\s/g, '').replace(/[^0-9]/g, '');

    if (value.length > 11) {
      value = value.slice(0, 11);
    }

    let formattedValue = '+7';

    for (let i = 1; i < value.length; i++) {
      if (i === 1 || i === 4 || i === 7 || i === 9) {
        formattedValue += ' ';
      }
      formattedValue += value[i];
    }

    setValue('phone', formattedValue);
    setPhone(formattedValue);
    setOperator(Number(formattedValue.slice(2, 6)));
  };

  const handleLabelClick = () => {
    setValue('phone', '+7');
    setPhone('');
    setOperator(undefined);
    if (inputRef.current) {
      inputRef.current.focus();
    }
  };

  const onSubmit = (data: PhoneFormInput) => {
    console.log('Submitted phone:', data.phone);

    setIsLoading(true);

    setTimeout(() => {
      navigate('/login-sms');
      setIsLoading(false);
    }, 1000);
  };

  const isButtonDisabled =
    phone.length !== 16 || (operator !== undefined && (operator < 900 || operator > 997));

  return (
    <div className="form">
      <div className="form__title">Авторизация</div>
      <Box
        className="form__block"
        onSubmit={handleSubmit(onSubmit)}
        component="form"
        sx={{ '& .MuiTextField-root': { width: '35ch' } }}
        autoComplete="off">
        <div className="form-inputs">
          <FormControl fullWidth error={!!errors.phone}>
            <div className="form__label">Номер телефона</div>
            <TextField
              value={phone}
              {...register('phone', { required: 'Введите номер телефона' })}
              onChange={handleInput}
              placeholder="+7"
              autoComplete="off"
              inputRef={inputRef}
              error={!!errors.phone}
              sx={{
                '& .MuiInputLabel-root': {
                  color: '#212d3a',
                },
                '& .MuiInputLabel-root.Mui-focused': {
                  color: '#212d3a',
                },
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
                  fontSize: '1.25rem',
                  color: '#212d3a',
                  height: '2ch',
                },
                '& .MuiInputBase-input::placeholder': {
                  color: '#212d3a',
                  fontSize: '1.25rem',
                  opacity: 0.8,
                },
              }}
              InputProps={{
                endAdornment: phone.length > 3 && (
                  <HighlightOffIcon
                    style={{ cursor: 'pointer', color: '#212d3a' }}
                    onClick={handleLabelClick}
                  />
                ),
              }}
            />
            <FormHelperText style={{ marginLeft: '12px' }}>{errors.phone?.message}</FormHelperText>
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
            padding: '10px 30px',
            borderRadius: '8px',
          }}
          type="submit"
          style={{ marginTop: '35px' }}
          variant="contained"
          disabled={isButtonDisabled}>
          {isLoading ? 'Загрузка...' : 'Продолжить'}
        </Button>
      </Box>
    </div>
  );
};
