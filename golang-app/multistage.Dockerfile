FROM golang:1.20 AS builder

WORKDIR /app

COPY . .

RUN go mod download

RUN go build -o main .

# This is the final image that will be used in production
FROM scratch

COPY --from=builder /app/main /app/main
CMD ["/app/main"]
