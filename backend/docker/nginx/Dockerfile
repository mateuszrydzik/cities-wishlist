FROM node:16.17-alpine AS build
WORKDIR /usr/src/app
COPY package.json package-lock.json ./
RUN npm install
COPY ./frontend .
RUN npm run build

FROM nginx:1.23.1
COPY --from=build /usr/src/app/dist/cities-wishlist /usr/share/nginx/html