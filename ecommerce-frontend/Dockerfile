# Dockerfile

# STAGE 1: Build stage
FROM node:18-alpine AS build

WORKDIR /app

# Copy package files
COPY package*.json ./

# Install dependencies
RUN npm ci --only=production

# Copy source code
COPY . .

# Pass the variable during build time because React embeds them in the JS bundle
ARG REACT_APP_API_URL=/api
ENV REACT_APP_API_URL=$REACT_APP_API_URL

# Build the application
RUN npm run build

# STAGE 2: SERVE. 
FROM nginx:stable-alpine
# Copy custom nginx configuration
COPY nginx.conf /etc/nginx/conf.d/default.conf
# Copy built output from the build stage to nginx html directory
COPY --from=build /app/build /usr/share/nginx/html

EXPOSE 80

# Start nginx server
CMD ["nginx", "-g", "daemon off;"]