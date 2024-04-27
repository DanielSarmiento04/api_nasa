# Use the official Nginx image
FROM nginx:latest

# # Remove the default Nginx configuration
RUN rm /etc/nginx/conf.d/default.conf

# # Copy your custom Nginx configuration
COPY nginx.conf /etc/nginx/conf.d/


# Copy the SSL certificates
COPY ./certificates/ser.key /etc/nginx/
COPY ./certificates/ser.pem /etc/nginx/


# Expose ports
EXPOSE 80
EXPOSE 443

# Set the default command to execute
CMD ["nginx", "-g", "daemon off;"]

