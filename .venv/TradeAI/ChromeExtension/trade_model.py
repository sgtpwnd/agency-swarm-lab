import torch
import torch.nn as nn
import torch.optim as optim

class TradeModel(nn.Module):
    def __init__(self, input_dim, hidden_dim, num_layers, dropout_rate):
        super(TradeModel, self).__init__()
        self.hidden_dim = hidden_dim
        self.num_layers = num_layers
        
        # LSTM layer
        if num_layers > 1:
            self.lstm = nn.LSTM(input_dim, hidden_dim, num_layers, batch_first=True, dropout=dropout_rate)
        else:
            self.lstm = nn.LSTM(input_dim, hidden_dim, num_layers, batch_first=True)
        
        # Dropout layer for regularization
        self.dropout = nn.Dropout(dropout_rate)
        
        # Fully connected layer
        self.fc = nn.Linear(hidden_dim, 1)
        
        # Activation function
        self.relu = nn.ReLU()

    def forward(self, x):
        # Initialize hidden and cell states
        h0 = torch.zeros(self.num_layers, x.size(0), self.hidden_dim).to(x.device)
        c0 = torch.zeros(self.num_layers, x.size(0), self.hidden_dim).to(x.device)
        
        # Forward propagate LSTM
        out, _ = self.lstm(x, (h0, c0))
        
        # Apply dropout to the output of the last time step
        out = self.dropout(out[:, -1, :])
        
        # Pass through the fully connected layer
        out = self.fc(out)
        
        # Apply ReLU activation function
        out = self.relu(out)
        return out

    def update_model(self, feedback, learning_rate=0.01):
        """
        Update the model parameters based on the feedback received from trade executions.
        Feedback should be a tensor with the same shape as model outputs, containing rewards or penalties.
        """
        self.train()
        optimizer = optim.Adam(self.parameters(), lr=learning_rate)
        loss_function = nn.MSELoss()

        # Calculate loss based on feedback (rewards or penalties)
        predicted = self(feedback['data'])
        loss = loss_function(predicted, feedback['rewards'])

        # Backpropagation
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

        print(f'Updated model parameters based on feedback. Loss: {loss.item():.4f}')

def train_model(model, train_loader, criterion, optimizer, num_epochs):
    model.train()
    for epoch in range(num_epochs):
        for inputs, targets in train_loader:
            inputs = inputs.to(device)
            targets = targets.to(device)
            
            outputs = model(inputs)
            loss = criterion(outputs, targets)
            
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()
            
            print(f'Epoch [{epoch+1}/{num_epochs}], Loss: {loss.item():.4f}')

# Example usage
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
model = TradeModel(input_dim=10, hidden_dim=50, num_layers=2, dropout_rate=0.3).to(device)
criterion = nn.MSELoss()
optimizer = optim.Adam(model.parameters(), lr=0.001)
# Assume train_loader is defined elsewhere
# train_model(model, train_loader, criterion, optimizer, num_epochs=50)